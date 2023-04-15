import {Component, OnInit} from '@angular/core';
import {Company} from "../models";
import {AllService} from "../all.service";

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit{

  companies: Company[] = []

  loaded: Boolean = false

  companyName: string = ''
  companyDescription: string = ''
  companyCity: string = ''
  companyAddress: string = ''
  companyImage: string = ''

  constructor(private appService: AllService) { }

  ngOnInit(): void {
    this.appService.getCompanies().subscribe((companies) => {
      this.companies = companies
      this.loaded = true
    })
  }

  addCompany() {
    if(this.companyImage == '') this.companyImage = 'https://st3.depositphotos.com/19428878/36416/v/450/depositphotos_364169666-stock-illustration-default-avatar-profile-icon-vector.jpg'
    this.appService.createCompany (
      this.companyName,
      this.companyDescription,
      this.companyCity,
      this.companyAddress,
      this.companyImage
    )
    .subscribe((company) => {
      this.companies.push(company)
      this.companyName = ''; this.companyDescription = '';
      this.companyCity = ''; this.companyAddress = '';
      this.companyImage = '';
    })
  }

  deleteCompany(id: number) {
    this.appService.deleteCompany(id).subscribe((company) => {
      this.companies = this.companies.filter((company) => company.id !== id)
    })
  }

  scrollDown() {
    window.scroll({top: 10000, behavior: "smooth"})
  }

}
