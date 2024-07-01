import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IceCreamInvitationComponent } from './ice-cream-invitation.component';

describe('IceCreamInvitationComponent', () => {
  let component: IceCreamInvitationComponent;
  let fixture: ComponentFixture<IceCreamInvitationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [IceCreamInvitationComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(IceCreamInvitationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
