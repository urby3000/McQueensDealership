import { Routes } from '@angular/router';
import { Home } from './home/home';
import { Login } from './login/login';
import { Carview } from './carview/carview';
import { Caraddedit } from './caraddedit/caraddedit';

export const routes: Routes = [
    {
        path: '',
        component: Home,
    },
    {
        path: 'login',
        component: Login,
    },
    {
        path: 'car/add',
        component: Caraddedit,
    },
    {
        path: 'car/:id',
        component: Carview
    },
    {
        path: 'car/:id/edit',
        component: Caraddedit,
    },
];
