import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Carview } from './carview';

describe('Carview', () => {
  let component: Carview;
  let fixture: ComponentFixture<Carview>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Carview]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Carview);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
