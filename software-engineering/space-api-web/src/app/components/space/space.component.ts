import { Component, OnInit } from '@angular/core';
import { HttpService } from 'src/app/services/http.service';
import { Joke } from 'src/app/models/Joke';
import { Space } from 'src/app/models/Space';

@Component({
  selector: 'app-space',
  templateUrl: './space.component.html',
  styleUrls: ['./space.component.css']
})
export class SpaceComponent implements OnInit {
  jokesData: Joke;
  spaceData: Space;

  constructor (private httpService: HttpService) {
  this.jokesData = {
        error: false,
        category: '',
        type: '',
        setup: '',
        delivery: '',
        flags: {
            nsfw: false,
            religious: false,
            political: false,
            racist: false,
            sexist: false,
            explicit: false
        },
        id: 0,
        safe: true,
        lang: ''
    }

    this.spaceData = {
      copyright: '',
      date: '',
      explanation: '',
      hdurl: '',
      media_type: '',
      service_version: '',
      title: '',
      url: ''
    }
  }

  ngOnInit(): void {
    this.httpService.getJokesData().subscribe(data => {
      this.jokesData = data;
    })
    this.httpService.getSpaceData().subscribe(data => {
      this.spaceData = data;
    })
  }

  showJoke(): void {
    alert(this.jokesData.setup);
    alert(this.jokesData.delivery);
  }
}

