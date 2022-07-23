import { TestBed } from '@angular/core/testing';

import { ClashApiService } from './clash-api.service';

describe('ClashApiService', () => {
  let service: ClashApiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ClashApiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
