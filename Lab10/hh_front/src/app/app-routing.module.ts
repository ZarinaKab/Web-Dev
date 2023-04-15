import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {CompaniesComponent} from "./companies/companies.component";
import {CompanyDetailComponent} from "./company-detail/company-detail.component";
import {CompanyVacanciesComponent} from "./company-vacancies/company-vacancies.component";
import {VacanciesComponent} from "./vacancies/vacancies.component";
import {VacancyDetailsComponent} from "./vacancy-details/vacancy-details.component";
import {TopTenVacanciesComponent} from "./top-ten-vacancies/top-ten-vacancies.component";

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'companies', component: CompaniesComponent },
  { path: 'companies/:id', component: CompanyDetailComponent },
  { path: 'companies/:id/vacancies', component: CompanyVacanciesComponent },
  { path: 'vacancies', component: VacanciesComponent },
  { path: 'vacancies/top-ten', component: TopTenVacanciesComponent },
  { path: 'vacancies/:id', component: VacancyDetailsComponent },
  { path: '', redirectTo: 'vacancies/top-ten', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
