import { Component, OnInit } from '@angular/core';
import {Company, Vacancy} from "../models";
import { ActivatedRoute } from "@angular/router";
import { AllService } from "../all.service";
import { Location } from '@angular/common';

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {

  company: Company

  companyName: string = ''
  companyDescription: string = ''
  companyCity: string = ''
  companyAddress: string = ''
  companyImage: string = ''

  vacancies: Vacancy[] = []

  constructor(private route: ActivatedRoute, private appService: AllService, private location: Location) {
    this.company = {} as Company
  }

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.appService.getCompany(id).subscribe( (company) => {
      this.company = company;
    })
    this.appService.getCompanyVacancies(id).subscribe((vacancies) => {
      this.vacancies = vacancies
    })
  }

  updateCompany(id: number) {
    if(this.companyName == '') this.companyName = this.company.name
    if(this.companyDescription == '') this.companyDescription = this.company.description
    if(this.companyCity == '') this.companyCity = this.company.city
    if(this.companyAddress == '') this.companyAddress = this.company.address
    if(this.companyImage == '') this.companyImage = this.company.image
    this.appService.updateCompany (
      id,
      this.companyName,
      this.companyDescription,
      this.companyCity,
      this.companyAddress,
      this.companyImage
    )
    .subscribe((company) => {
      this.company.name = company.name
      this.company.description = company.description
      this.company.city = company.city
      this.company.address = company.address
      this.company.image = company.image
    })
  }

  returnBack() {
    this.location.back()
  }

}
