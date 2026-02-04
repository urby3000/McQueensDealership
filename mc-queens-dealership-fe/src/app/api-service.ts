import { JwtHelperService, JWT_OPTIONS } from '@auth0/angular-jwt';
import { HttpClient, HttpParams } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { Car, CarsList, User, FilterArg } from './interfaces';
import { Router } from '@angular/router';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  public api_url = 'http://localhost:5000'; // API URL

  constructor(private router: Router, private http: HttpClient, private readonly jwtHelper: JwtHelperService) { }

  // const headers = { 'Authorization': 'Bearer my-token', 'My-Custom-Header': 'foobar' };


  getCars(per_page:number, get_page:number, filters:FilterArg[]): Observable<CarsList> {
    let baseParams = new HttpParams().set('per_page', per_page).set('page', get_page);
    filters.forEach(f => {
      baseParams = baseParams.append(f.name,f.value);
    });
    return this.http.get<CarsList>(`${this.api_url}/cars`, {
      params: baseParams,
    });
  }
  getCar(id: number): Observable<Car> {
    return this.http.get<Car>(`${this.api_url}/car/${id}`);
  }
  like(car_id:string){
    let headers = { 'Authorization': 'Bearer ' }
    if(this.isAuthenticated()){
      let token = localStorage.getItem('access_token')
      headers = { 'Authorization': 'Bearer ' + token }
    }
    return this.http.get<any>(`${this.api_url}/car/${car_id}/like`, { headers });
  }
  unlike(car_id:string){
    let headers = { 'Authorization': 'Bearer ' }
    if(this.isAuthenticated()){
      let token = localStorage.getItem('access_token')
      headers = { 'Authorization': 'Bearer ' + token }
    }
    return this.http.delete<any>(`${this.api_url}/car/${car_id}/unlike`, { headers });
  }
  createCar(brand: string, model: string, year: string, price: string, fuel: string, doors: string, description: string, file: File) {
    const form = new FormData;
    form.append('brand', brand);
    form.append('model', model);
    form.append('year', year);
    form.append('price', price);
    form.append('fuel_type', fuel);
    form.append('doors', doors);
    form.append('description', description);
    form.append('image', file)
    let headers = { 'Authorization': 'Bearer ' }
    if (this.isAuthenticated()) {
      let token = localStorage.getItem('access_token')
      headers = { 'Authorization': 'Bearer ' + token }
    }
    return this.http.post<any>(`${this.api_url}/car/create`, form, { headers });

  }
  editCar(car_id: string, brand: string, model: string, year: string, price: string, fuel: string, doors: string, description: string, file: File) {
    const form = new FormData;
    form.append('brand', brand);
    form.append('model', model);
    form.append('year', year);
    form.append('price', price);
    form.append('fuel_type', fuel);
    form.append('doors', doors);
    form.append('description', description);
    form.append('image', file)
    let headers = { 'Authorization': 'Bearer ' }
    if (this.isAuthenticated()) {
      let token = localStorage.getItem('access_token')
      headers = { 'Authorization': 'Bearer ' + token }
    }
    return this.http.post<any>(`${this.api_url}/car/${car_id}/edit`, form, { headers });

  }
  deleteCar(car_id: string) {
    let headers = { 'Authorization': 'Bearer ' }
    if (this.isAuthenticated()) {
      let token = localStorage.getItem('access_token')
      headers = { 'Authorization': 'Bearer ' + token }
    }
    return this.http.delete<any>(`${this.api_url}/car/${car_id}/delete`, { headers });
  }
  public login(email: string, password: string) {
    const form = new FormData;
    form.append('email', email);
    form.append('password', password);
    let subject = new Subject<string>();
    this.http.post<any>(`${this.api_url}/user/login`, form).subscribe((data) => {
      if (data.access_token) {
        localStorage.setItem('access_token', data.access_token);
        localStorage.setItem('user_email', data.email);
        localStorage.setItem('user_id', data.user_id);
        localStorage.setItem('is_admin', data.is_admin);
        this.router.navigate(['/']);
      } else {
        subject.next(data.err);
      }

    })
    return subject;
  }
  public register(email: string, password: string) {
    const form = new FormData;
    form.append('email', email);
    form.append('password', password);

    return this.http.post<any>(`${this.api_url}/user/create`, form);
  }
  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user_email');
    localStorage.removeItem('user_id');
    this.router.navigate(['/login']);
  }
  userId() {
    return localStorage.getItem('user_id');
  }
  userEmail() {
    return localStorage.getItem('user_email');
  }
  isAdmin() {
    let admin;
    if (this.isAuthenticated()) {
      admin = localStorage.getItem('is_admin');
    }
    return admin;
  }
  isAuthenticated() {
    if (typeof window !== 'undefined' && localStorage) {
      const token = localStorage.getItem('access_token');
      return !this.jwtHelper.isTokenExpired(token);
    }
    return false;
  }
}
