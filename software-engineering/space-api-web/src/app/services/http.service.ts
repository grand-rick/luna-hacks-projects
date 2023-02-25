import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Space } from 'src/app/models/Space';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private http: HttpClient) { }

  getSpaceData(): Observable<Space[]> {
    return this.http.get<Space[]>('https://api.nasa.gov/planetary/apod?api_key=YDeOIxQjJY2fHA4faKCiSKESNydHaU3vldwNufy2');
  }
}
