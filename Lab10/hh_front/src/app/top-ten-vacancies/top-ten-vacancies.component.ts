import {Component, OnInit} from '@angular/core';
import {Vacancy} from "../models";
import {AllService} from "../all.service";

@Component({
  selector: 'app-top-ten-vacancies',
  templateUrl: './top-ten-vacancies.component.html',
  styleUrls: ['./top-ten-vacancies.component.css']
})
export class TopTenVacanciesComponent implements OnInit {

  vacancies: Vacancy[] = []

  loaded: Boolean = false
  index = 0

  constructor(private appService: AllService) { }

  ngOnInit(): void {
    this.appService.getTopTenVacancies().subscribe((vacancies) => {
      this.vacancies = vacancies
      this.loaded = true
    })
  }

}
