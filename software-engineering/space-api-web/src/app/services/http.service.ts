import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Joke } from 'src/app/models/Joke';
import { Space } from 'src/app/models/Space';

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  key: string = 'jGa8x7CUNmirtWcIymkmqOJuFIDg9vuNitcrMF7I';

  constructor(private http: HttpClient) { }

  getJokesData(): Observable<Joke> {
    return this.http.get<Joke>('https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist,explicit');
  }

  getSpaceData(): Observable<Space> {
    return this.http.get<Space>(`https://api.nasa.gov/planetary/apod?api_key=${this.key}`);
  }
}
