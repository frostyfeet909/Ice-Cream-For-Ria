import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { IceCreamInvitationComponent } from './ice-cream-invitation/ice-cream-invitation.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, IceCreamInvitationComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Ice Cream Invitation';
}
