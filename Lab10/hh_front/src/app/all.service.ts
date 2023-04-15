import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import {Company, Vacancy} from "./models";
import { HttpClient } from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class AllService {

  BASE_URL = 'http://127.0.0.1:8000'

  constructor(private client: HttpClient) { }

  getCompanies(): Observable<Company[]> {
    return this.client.get<Company[]>(`${this.BASE_URL}/api/companies`)
  }

  getCompany(id: number): Observable<Company> {
    return this.client.get<Company>(`${this.BASE_URL}/api/companies/${id}`)
  }

  createCompany (
    companyName: string,
    companyDescription: string,
    companyCity: string,
    companyAddress: string,
    companyImage: string
  ): Observable<Company> {
    return this.client.post<Company>(
      `${this.BASE_URL}/api/companies`,
      {
        name: companyName,
        description: companyDescription,
        city: companyCity,
        address: companyAddress,
        image: companyImage
      }
    )
  }

  updateCompany (
    id: number,
    companyName: string,
    companyDescription: string,
    companyCity: string,
    companyAddress: string,
    companyImage: string
  ): Observable<Company> {
    return this.client.put<Company>(
      `${this.BASE_URL}/api/companies/${id}`,
      {
        name: companyName,
        description: companyDescription,
        city: companyCity,
        address: companyAddress,
        image: companyImage
      }
    )
  }

  deleteCompany(id: number): Observable<any> {
    return this.client.delete(`${this.BASE_URL}/api/companies/${id}`)
  }



  // Vacancies
  getVacancies(): Observable<Vacancy[]> {
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/api/vacancies`)
  }

  getVacancy(id: number): Observable<Vacancy> {
    return this.client.get<Vacancy>(`${this.BASE_URL}/api/vacancies/${id}`)
  }

  createVacancy (
    vacancyName: string,
    vacancyDescription: string,
    vacancySalary: number,
    vacancyCompanyId: number,
    vacancyImage: string
  ): Observable<Vacancy> {
    return this.client.post<Vacancy>(
      `${this.BASE_URL}/api/vacancies/`,
      {
        name: vacancyName,
        description: vacancyDescription,
        salary: vacancySalary,
        company_id: vacancyCompanyId,
        image: vacancyImage
      }
    )
  }

  updateVacancy (
    id: number,
    vacancyName: string,
    vacancyDescription: string,
    vacancySalary: number,
    vacancyCompanyId: number,
    vacancyImage: string
  ): Observable<Vacancy> {
    return this.client.put<Vacancy>(
      `${this.BASE_URL}/api/vacancies/${id}`,
      {
        name: vacancyName,
        description: vacancyDescription,
        salary: vacancySalary,
        company_id: vacancyCompanyId,
        image: vacancyImage
      }
    )
  }

  deleteVacancy(id: number): Observable<any> {
    return this.client.delete(`${this.BASE_URL}/api/vacancies/${id}`)
  }

  getCompanyVacancies(id: number) {
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies`)
  }

  getTopTenVacancies(): Observable<Vacancy[]> {
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/api/vacancies/top_ten`)
  }

}
