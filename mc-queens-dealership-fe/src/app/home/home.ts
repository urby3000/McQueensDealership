import { ChangeDetectorRef, Component, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { RouterLink } from "@angular/router";
import { ApiService } from '../api-service';
import { CarsList, Car, Pagination, FilterArg, Like } from '../interfaces';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { NgClass } from '@angular/common';

@Component({
  selector: 'app-home',
  imports: [RouterLink, ReactiveFormsModule, NgClass],
  templateUrl: './home.html',
  styleUrl: './home.css',
})
export class Home implements OnInit {

  constructor(public apiService: ApiService, private cd: ChangeDetectorRef) {
  }
  /*italian hand gesture*/pagination_iteration/*italian hand gesture*/: number[] = [8, 12, 24, 48, 96]
  per_page = 24;
  get_page = 1;

  sort_iterations: string[] = ["none", "desc", "asc"];
  current_sort_brand = "none";
  current_sort_year = "none";
  current_sort_price = "none";

  filter_show_liked = false;
  filter_add_brand = new FormControl('');
  filter_min_price = new FormControl('');
  filter_max_price = new FormControl('');
  filter_brands: string[] = [];
  min_price_saved: string = "";
  max_price_saved: string = "";
  car_image_home_url = "";
  cars: Car[] = [];
  pagination_info: Pagination = ({} as any) as Pagination;

  ngOnInit(): void {
    this.per_page = this.pagination_iteration[1];
    this.car_image_home_url = this.apiService.api_url;
    this.getCarList();
  }

  getCarList(): void {
    this.apiService.getCars(this.per_page, this.get_page, this.create_filter_sort_arg_array()).subscribe(
      (data) => {
        this.cars = data.results;
        this.pagination_info = data.pagination;
        this.get_page = this.pagination_info.page;
        this.cd.detectChanges();
      }
    );
  }
  like(car_id: string): void {
    this.apiService.like(car_id).subscribe(
      (data) => {
        this.getCarList();
      }
    );

  }
  unlike(car_id: string): void {
    this.apiService.unlike(car_id).subscribe(
      (data) => {
        this.getCarList();
      }
    );

  }
  doiLikeThisCar(car: Car): boolean {
    for (let l of car.likes) {
      if (l.user_id.toString() == this.apiService.userId()) {
        return true;
      }
    }
    return false;
  }
  create_filter_sort_arg_array(): FilterArg[] {
    let arr: FilterArg[] = [];
    //filters
    this.filter_brands.forEach(b => {
      arr.push({ name: "brand", value: b });
    });
    if (this.min_price_saved != "") {
      arr.push({ name: "min_price", value: this.min_price_saved });
    }
    if (this.max_price_saved != "") {
      arr.push({ name: "max_price", value: this.max_price_saved });
    }
    //sorts
    if (this.current_sort_brand != "none") {
      arr.push({ name: "sortbrand" + this.current_sort_brand, value: "true" });
    }
    if (this.current_sort_price != "none") {
      arr.push({ name: "sortprice" + this.current_sort_price, value: "true" });
    }
    if (this.current_sort_year != "none") {
      arr.push({ name: "sortyear" + this.current_sort_year, value: "true" });
    }
    if (this.filter_show_liked) {
      arr.push({ name: "likes", value: "likes" });
      arr.push({ name: "user_id" , value: this.apiService.userId() || "" });
    }
    return arr;
  }
  add_filters(): void {
    if (this.filter_add_brand.value && !this.filter_brands.includes(this.filter_add_brand.value)) {
      this.filter_brands.push(this.filter_add_brand.value);
    }
    if (this.filter_min_price.value) {
      this.min_price_saved = this.filter_min_price.value;
    }
    if (this.filter_max_price.value) {
      this.max_price_saved = this.filter_max_price.value;
    }
    this.getCarList();
  }
  filter_brand_remove(brand: string): void {
    const index = this.filter_brands.indexOf(brand, 0);
    if (index > -1) {
      this.filter_brands.splice(index, 1);
    }
    this.getCarList();
  }
  filter_min_price_remove(): void {
    this.min_price_saved = "";
    this.getCarList();
  }
  filter_max_price_remove(): void {
    this.max_price_saved = "";
    this.getCarList();
  }
  change_results_per_page(): void {
    let index = this.pagination_iteration.indexOf(this.per_page, 0);
    index = index + 1;
    if (index > this.pagination_iteration.length - 1) {
      index = 0
    }
    this.per_page = this.pagination_iteration[index];
    this.get_page = 1;
    this.getCarList();
  }
  prev_page(): void {
    if (this.get_page - 1 == 0) {
      this.get_page = 1;
    }
    else {
      this.get_page = this.get_page - 1;
    }
    this.getCarList();
  }
  next_page(): void {
    if (this.get_page + 1 > this.pagination_info.pages) {
      this.get_page = this.pagination_info.pages;
    }
    else {
      this.get_page = this.get_page + 1;
    }
    this.getCarList();
  }
  sort_brand(): void {
    let index = this.sort_iterations.indexOf(this.current_sort_brand, 0);
    index = index + 1;
    if (index > this.sort_iterations.length - 1) {
      index = 0
    }
    this.current_sort_brand = this.sort_iterations[index];
    this.getCarList();
  }
  sort_year(): void {
    let index = this.sort_iterations.indexOf(this.current_sort_year, 0);
    index = index + 1;
    if (index > this.sort_iterations.length - 1) {
      index = 0
    }
    this.current_sort_year = this.sort_iterations[index];
    this.getCarList();
  }
  sort_price(): void {
    let index = this.sort_iterations.indexOf(this.current_sort_price, 0);
    index = index + 1;
    if (index > this.sort_iterations.length - 1) {
      index = 0
    }
    this.current_sort_price = this.sort_iterations[index];
    this.getCarList();

  }
  toggle_liked():void {
    this.filter_show_liked = !this.filter_show_liked;
    this.getCarList();
  }

}
