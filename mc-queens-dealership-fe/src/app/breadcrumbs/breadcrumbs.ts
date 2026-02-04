import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { ApiService } from '../api-service';

@Component({
  selector: 'app-breadcrumbs',
  imports: [RouterLink],
  templateUrl: './breadcrumbs.html',
  styleUrl: './breadcrumbs.css',
})
export class Breadcrumbs implements OnInit {
    constructor(public apiService: ApiService) {
  }

  ngOnInit(): void {
   
  }

  logout(){
    this.apiService.logout();
  }
}
