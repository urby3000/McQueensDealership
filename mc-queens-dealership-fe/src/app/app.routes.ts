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
    //temp -> TODO car routes...
    {
        path: 'car',
        component: Carview,
    },
    {
        path: 'caraddedit',
        component: Caraddedit,
    },
];
