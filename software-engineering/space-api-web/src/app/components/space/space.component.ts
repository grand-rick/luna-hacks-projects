import { Component, OnInit } from '@angular/core';
import { HttpService } from 'src/app/services/http.service';
import { Space } from 'src/app/models/Space';

@Component({
  selector: 'app-space',
  templateUrl: './space.component.html',
  styleUrls: ['./space.component.css']
})
export class SpaceComponent implements OnInit {
  spaceData: Space[] = [];
  data: Space = this.getSpaceData();

  constructor (private httpService: HttpService) {}

  ngOnInit(): void {
    this.httpService.getSpaceData().subscribe(data => {
      this.spaceData = data;
    })
  }

  getSpaceData(): Space {
    const data = this.spaceData[0];
    return data;
  }
}
