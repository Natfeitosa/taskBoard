import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";

@Injectable({
    providedIn: 'root'
})

export class UserService{
    private baseURL = 'http://localhost:8000'
    constructor(private http: HttpClient) {}

    userLogin(username: string, password: string): Observable<any>{
        const body = {username, password};
        return this.http.post<any>(this.baseURL + '/login', body);
    }

    getAllProjects(): Observable<any>{
        return this.http.get<any>(this.baseURL + '/projects');
    }
}