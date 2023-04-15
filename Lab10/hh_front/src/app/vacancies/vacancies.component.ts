import {Component, OnInit} from '@angular/core';
import {Company, Vacancy} from "../models";
import { AllService } from "../all.service";

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent implements OnInit {

  vacancies: Vacancy[] = []

  vacancyName: string = ''
  vacancyDescription: string = ''
  vacancySalary: number = 0
  vacancyCompanyId: number = 0
  vacancyImage: string = ''

  loaded: Boolean = false

  constructor(private appService: AllService) { }

  ngOnInit(): void {
    this.appService.getVacancies().subscribe((vacancies) => {
      this.vacancies = vacancies
      this.loaded = true
    })
  }

  addVacancy() {
    if(this.vacancyImage == '') this.vacancyImage = 'https://st3.depositphotos.com/19428878/36416/v/450/depositphotos_364169666-stock-illustration-default-avatar-profile-icon-vector.jpg'
    this.appService.createVacancy (
      this.vacancyName,
      this.vacancyDescription,
      this.vacancySalary,
      this.vacancyCompanyId,
      this.vacancyImage
    )
    .subscribe((vacancy) => {
      this.vacancies.push(vacancy)
      this.vacancyName = ''; this.vacancyDescription = '';
      this.vacancySalary = 0; this.vacancyCompanyId = 0;
      this.vacancyImage = '';
    })
  }

  deleteVacancy(id: number) {
    this.appService.deleteVacancy(id).subscribe((vacancy) => {
      this.vacancies = this.vacancies.filter((vacancy) => vacancy.id !== id)
    })
  }

  scrollDown() {
    window.scroll({top: 10000, behavior: "smooth"})
  }

}
