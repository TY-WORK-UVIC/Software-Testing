let cities=[];

function initializeCityDatabase(){
    cities.push('Vienna');
    cities.push('San Juan');

}

function clearCityDatabase(){
    cities=[];
}

function isCity(name){
    return cities.includes(name);
}


beforeEach(() => {
    initializeCityDatabase();
  });
  
  afterEach(() => {
    clearCityDatabase();
  });
  
  test('city database has Vienna', () => {
    expect(isCity('Vienna')).toBeTruthy();
  });
  
  test('city database has San Juan', () => {
    expect(isCity('San Juan')).toBeTruthy();
  });