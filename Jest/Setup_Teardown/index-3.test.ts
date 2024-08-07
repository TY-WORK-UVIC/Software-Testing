let globalvariable='A';




test('first test', () => {
    expect(globalvariable).toBe('A');
    globalvariable='B';
  });
  
  test.only('second test', () => {
    expect(globalvariable).toBe('A');
  });