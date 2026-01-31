import { Component, inject } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-header',
  imports: [],
  templateUrl: './header.html',
  styleUrl: './header.css',
})
export class Header {
  currentRoute: string = "";
  constructor(private router: Router) {
  }
    ngOnInit() {

    this.currentRoute = this.router.url;

  }
}
