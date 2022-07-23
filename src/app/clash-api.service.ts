import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
	providedIn: 'root'
})
export class ClashApiService {

	readonly API_URL = 'http://localhost:5000';

	constructor(private http: HttpClient) { }

	getDeck(player: string, trophies: string): Observable<any> {
		return this.http.get<any>(
			`${this.API_URL}/api/v1/deck?player=${player}&trophies=${trophies}`,
			{
				headers: new HttpHeaders({
					'Content-Type': 'application/json',
					'Accept': 'application/json',
				})
			}
		);
	}
}
