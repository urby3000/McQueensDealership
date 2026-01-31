import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Caraddedit } from './caraddedit';

describe('Caraddedit', () => {
  let component: Caraddedit;
  let fixture: ComponentFixture<Caraddedit>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Caraddedit]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Caraddedit);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
