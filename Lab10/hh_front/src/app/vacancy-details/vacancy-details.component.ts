import {Component, OnInit} from '@angular/core';
import {Company, Vacancy} from "../models";
import {ActivatedRoute} from "@angular/router";
import {AllService} from "../all.service";
import {Location} from "@angular/common";

@Component({
  selector: 'app-vacancy-details',
  templateUrl: './vacancy-details.component.html',
  styleUrls: ['./vacancy-details.component.css']
})
export class VacancyDetailsComponent implements OnInit {

  vacancy: Vacancy

  vacancyName: string = ''
  vacancyDescription: string = ''
  vacancySalary: number = 0
  vacancyCompanyId: number = 0
  vacancyImage: string = ''

  constructor(private route: ActivatedRoute, private appService: AllService, private location: Location) {
    this.vacancy = {} as Vacancy
  }

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.appService.getVacancy(id).subscribe( (vacancy) => {
      this.vacancy = vacancy;
    })
  }

  updateVacancy(id: number) {
    if(this.vacancyName == '') this.vacancyName = this.vacancy.name
    if(this.vacancyDescription == '') this.vacancyDescription = this.vacancy.description
    if(this.vacancySalary == 0) this.vacancySalary = this.vacancy.salary
    if(this.vacancyCompanyId == 0) this.vacancyCompanyId = this.vacancy.company.id
    if(this.vacancyImage == '') this.vacancyImage = this.vacancy.image
    this.appService.updateVacancy (
      id,
      this.vacancyName,
      this.vacancyDescription,
      this.vacancySalary,
      this.vacancyCompanyId,
      this.vacancyImage
    )
    .subscribe((vacancy) => {
      this.vacancy.name = vacancy.name
      this.vacancy.description = vacancy.description
      this.vacancy.salary = vacancy.salary
      this.vacancy.company = vacancy.company
      this.vacancy.image = vacancy.image
    })
  }

  returnBack() {
    this.location.back()
  }

}
