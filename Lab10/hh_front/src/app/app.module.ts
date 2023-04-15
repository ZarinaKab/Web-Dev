import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { CompaniesComponent } from './companies/companies.component';
import { CompanyDetailComponent } from './company-detail/company-detail.component';
import { CompanyVacanciesComponent } from './company-vacancies/company-vacancies.component';
import { VacanciesComponent } from './vacancies/vacancies.component';
import { VacancyDetailsComponent } from './vacancy-details/vacancy-details.component';
import { TopTenVacanciesComponent } from './top-ten-vacancies/top-ten-vacancies.component';
import {HttpClientModule} from "@angular/common/http";
import {FormsModule} from "@angular/forms";

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CompaniesComponent,
    CompanyDetailComponent,
    CompanyVacanciesComponent,
    VacanciesComponent,
    VacancyDetailsComponent,
    TopTenVacanciesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
