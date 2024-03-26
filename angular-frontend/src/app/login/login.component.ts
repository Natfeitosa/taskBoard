import { Component, Injectable } from '@angular/core';
import {FormGroup, FormControl, ReactiveFormsModule, Validators} from '@angular/forms';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
  standalone: true,
  imports: [ReactiveFormsModule]
})

export class LoginComponent {
  loginForm = new FormGroup({
    email: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required),
  })
 
  constructor(private loginService: UserService, private router: Router){}

  login() {
    const email = this.loginForm.get('email')?.value!;
    const password = this.loginForm.get('password')?.value!;

    this.loginService.userLogin(email, password).subscribe({
    next: response => {
      console.log(response),
      this.router.navigate(['/projects']);
    },
    error: error => console.log(error)
  });
}}