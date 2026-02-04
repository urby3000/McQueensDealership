import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from '../api-service';

@Component({
  selector: 'app-login',
  imports: [ReactiveFormsModule],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login implements OnInit {
  
  login_err = "";
  login_email = new FormControl('', [Validators.required]);
  login_password = new FormControl('', [Validators.required]);


  create_err = "";
  create_succ = false;
  create_email = new FormControl('', [Validators.required]);
  create_password = new FormControl('', [Validators.required]);
  create_password_confirm = new FormControl('', [Validators.required]);


  constructor(private apiService: ApiService,
    private router: Router) {
  }

  ngOnInit(): void {
    
  }

  login() {
    this.login_err = "";
    if (this.login_email.value && this.login_password.value) {
      this.apiService.login(this.login_email.value, this.login_password.value).subscribe({
        next: (v) => {
          this.login_err = v;
        },
      });
    }
  }
  register() {
    this.create_err = "";
    this.create_succ = false;
    if (this.create_email.value && this.create_password.value ) {
      if(this.create_password.value != this.create_password_confirm.value){
        this.create_err = "Passwords don't match. :(";
        return;
      }
      this.apiService.register(this.create_email.value, this.create_password.value).subscribe((data) => {
        if (data.msg) {//created
          this.create_succ = true;
        } else {//err data.err
          this.create_err = data.err
        }
      });
    }
  }
}
