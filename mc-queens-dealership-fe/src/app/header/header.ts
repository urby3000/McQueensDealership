import { Component, inject, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';

@Component({
  selector: 'app-header',
  imports: [],
  templateUrl: './header.html',
  styleUrl: './header.css',
})
export class Header implements OnInit  {
  currentRoute: string = "";
  constructor(private router: Router) {
  }
    ngOnInit() {

    this.currentRoute = this.router.url;

  }
}
