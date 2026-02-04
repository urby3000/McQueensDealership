import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { ApiService } from '../api-service';
import { Car } from '../interfaces';
import { NgClass } from '@angular/common';

@Component({
  selector: 'app-carview',
  imports: [RouterLink, NgClass],
  templateUrl: './carview.html',
  styleUrl: './carview.css',
})
export class Carview implements OnInit {
  car_image_home_url = "";
  car_id = 0;
  car: Car = ({} as any) as Car;
  constructor(public apiService: ApiService,
    private router: Router, private route: ActivatedRoute, private cd: ChangeDetectorRef) {
  }
  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.car_id = params['id']; // Access the 'id' parameter from the URL
    });
    this.getCar();
    this.car_image_home_url = this.apiService.api_url;
  }
  getCar(): void {
    this.apiService.getCar(this.car_id).subscribe(
      (data) => {
        this.car = data;
        this.cd.detectChanges();
      }
    );
  }

  doiLikeThisCar(car: Car): boolean {
    if(car.likes){
        for (let l of car.likes) {
          if (l.user_id.toString() == this.apiService.userId()) {
            return true;
          }
        }
        return false;
    }
        return false;
  }

  like(car_id: string): void {
    this.apiService.like(car_id).subscribe(
      (data) => {
          this.getCar();
          this.cd.detectChanges();
      }
    );

  }
  unlike(car_id: string): void {
    this.apiService.unlike(car_id).subscribe(
      (data) => {
          this.getCar();
          this.cd.detectChanges();
      }
    );

  }
}
