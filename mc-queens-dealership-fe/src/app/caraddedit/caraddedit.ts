import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { FormControl, ReactiveFormsModule, Validators } from '@angular/forms';
import { ApiService } from '../api-service';
import { ActivatedRoute, Event, Route, Router } from '@angular/router';
import { Car } from '../interfaces';

@Component({
  selector: 'app-caraddedit',
  imports: [ReactiveFormsModule],
  templateUrl: './caraddedit.html',
  styleUrl: './caraddedit.css',
})
export class Caraddedit implements OnInit {

  img_preview = "";
  is_edit = false;
  create_err = false;
  car: Car = ({} as any) as Car;
  car_id = 0;
  car_image_home_url = "";

  constructor(private apiService: ApiService, public route: ActivatedRoute, private router: Router,  private cd: ChangeDetectorRef) {
    if (route.snapshot.url[1].path != "add") {
      this.is_edit = true
    }
  }
  brand = new FormControl('', [Validators.required]);
  model = new FormControl('', [Validators.required]);
  year = new FormControl('', [Validators.required]);
  price = new FormControl('', [Validators.required]);
  fuel = new FormControl('', [Validators.required]);
  doors = new FormControl('', [Validators.required]);
  desc = new FormControl('', [Validators.required]);
  file = {} as File;

  ngOnInit(): void {
    if (this.is_edit) {
      this.route.params.subscribe(params => {
        this.car_id = params['id']; // Access the 'id' parameter from the URL
      });
      this.getCar();
      this.car_image_home_url = this.apiService.api_url;
    }
  }

  getCar(): void {
    this.apiService.getCar(this.car_id).subscribe(
      (data) => {
        this.car = data;
        this.brand.setValue(this.car.brand);
        this.model.setValue(this.car.model);
        this.year.setValue(this.car.year.toString());
        this.price.setValue(this.car.price.toString());
        this.fuel.setValue(this.car.fuel_type.toString());
        this.doors.setValue(this.car.doors.toString());
        this.desc.setValue(this.car.description);
        this.cd.detectChanges();
      }
    );
  }
  deleteCar() {
      if (this.is_edit) {
        this.apiService.deleteCar(this.car.id.toString()).subscribe((data) => {
            if (data.msg) {//deleted
              this.router.navigate(['/']);
            } 
          });
      }
  }
  onFileSelected(event: any) {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files.length > 0) {
      this.file = target.files[0];
      this.imagePreview();
    }

  }
  createEditCar() {
    this.create_err = false;
    if (this.brand.value && this.model.value && this.year.value
      && this.price.value && this.fuel.value && this.doors.value && this.desc.value && this.file
    ) {
      if (this.is_edit) {
        this.apiService.editCar(this.car.id.toString(), this.brand.value, this.model.value, this.year.value, this.price.value,
          this.fuel.value, this.doors.value, this.desc.value, this.file).subscribe((data) => {
            if (data.msg) {//edited
              this.getCar();
              this.cd.detectChanges();
            } 
          });
      } else {
        this.apiService.createCar(this.brand.value, this.model.value, this.year.value, this.price.value,
          this.fuel.value, this.doors.value, this.desc.value, this.file).subscribe((data) => {
            if (data.msg) {//created
              this.router.navigate(['/']);
            } 
          });
      }
    } else {
      this.create_err = true;
    }
  }

  imagePreview(): void {
  this.img_preview = '';
  if (this.file) {
    const reader = new FileReader();
    reader.onload = (e: any) => {
      this.img_preview = e.target.result;
      this.cd.detectChanges();
    };
    reader.readAsDataURL(this.file);
  }
}


}
