import { Component } from '@angular/core';
import { ConfettiService } from '../confetti.service';

@Component({
  selector: 'app-ice-cream-invitation',
  standalone: true,
  imports: [],
  templateUrl: './ice-cream-invitation.component.html',
  styleUrl: './ice-cream-invitation.component.css'
})
export class IceCreamInvitationComponent {
  constructor(public confettiService: ConfettiService) {}
}
