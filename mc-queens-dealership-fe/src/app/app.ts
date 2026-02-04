import { ChangeDetectorRef, Component, OnInit, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Header } from './header/header';
import { Footer } from "./footer/footer";
import { Breadcrumbs } from './breadcrumbs/breadcrumbs';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Footer, Header, Breadcrumbs],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('mc-queens-dealership-fe');
}
