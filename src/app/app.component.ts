import { Component, HostListener } from '@angular/core';
import { ClashApiService } from './clash-api.service';
import {DomSanitizer} from '@angular/platform-browser';

@Component({
	selector: 'app-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.less']
})
export class AppComponent {
	player: string = '';
	trophies: string = '';
	deck: any = [];
	showLoading: boolean = false;
	showOverlay: boolean = false;

	constructor(private clashApi: ClashApiService, private sanitizer:DomSanitizer) { }

	ngOnInit() {
	}

	@HostListener('document:keypress', ['$event'])
	handleKeyboardEvent(event: KeyboardEvent) {
		if (event.key === 'Enter') {
			this.clashApi.getDeck(this.player, this.trophies).subscribe(
				deck => {
					if (deck == null) {
						alert(`No deck found for ${this.player} with ${this.trophies} trophies`);
					}
					this.deck = deck;
					this.showLoading = false;
				}
			)
			this.showLoading = true;
		}
	}

	showInfo() {
		this.showOverlay = true;
	}

	closeInfo() {
		this.showOverlay = false;
	}

	sanitize(url:string){
		return this.sanitizer.bypassSecurityTrustUrl(url);
	}
}
