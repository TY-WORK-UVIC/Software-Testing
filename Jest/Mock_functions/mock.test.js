function forEach(items, callback) {
    for (const item of items) {
      callback(item);
    }
  }

// const forEach = require('./forEach');

const mockCallback = jest.fn(x => 42 + x);

test('forEach mock function', () => {
  forEach([0, 1], mockCallback);

  // The mock function was called twice
  expect(mockCallback.mock.calls).toHaveLength(2);

  // The first argument of the first call to the function was 0
  expect(mockCallback.mock.calls[0][0]).toBe(0);

  // The first argument of the second call to the function was 1
  expect(mockCallback.mock.calls[1][0]).toBe(1);

  // The return value of the first call to the function was 42
  expect(mockCallback.mock.results[0].value).toBe(42);
});


test('this', ()=> {
    const myMock1 = jest.fn();
const a = new myMock1();
console.log(myMock1.mock.instances);
// > [ <a> ]

const myMock2 = jest.fn();
const b = {};
b.name= "b";
const bound = myMock2.bind(b);
bound();
console.log(myMock2.mock.contexts);
// > [ <b> ]
})

test('someMockFunction', ()=> {
    // The function was called exactly once
const someMockFunction=jest.fn(()=> 'return value');

someMockFunction('first arg','second arg');
expect(someMockFunction.mock.calls).toHaveLength(1);

// The first arg of the first call to the function was 'first arg'
expect(someMockFunction.mock.calls[0][0]).toBe('first arg');

// The second arg of the first call to the function was 'second arg'
expect(someMockFunction.mock.calls[0][1]).toBe('second arg');

// The return value of the first call to the function was 'return value'
expect(someMockFunction.mock.results[0].value).toBe('return value');

const someMockConstructor=  jest.fn();
const a= new someMockConstructor();
a.name='test';
const b= new someMockConstructor();


// The function was called with a certain `this` context: the `element` object.
// expect(someMockConstructor.mock.contexts[0]).toBe(element);

// This function was instantiated exactly twice
expect(someMockConstructor.mock.instances.length).toBe(2);

// The object returned by the first instantiation of this function
// had a `name` property whose value was set to 'test'
expect(someMockConstructor.mock.instances[0].name).toBe('test');



})

test("", ()=> {
    const myMock = jest.fn();
console.log(myMock());
// > undefined

myMock.mockReturnValueOnce(10).mockReturnValueOnce('x').mockReturnValue(true);

console.log(myMock(), myMock(), myMock(), myMock());
// > 10, 'x', true, true
})

test('filertest', ()=>{
    const filterTestFn = jest.fn();

// Make the mock return `true` for the first call,
// and `false` for the second call
filterTestFn.mockReturnValueOnce(true).mockReturnValueOnce(false);

const result = [11, 12].filter(num => filterTestFn(num));

console.log(result);
// > [11]
console.log(filterTestFn.mock.calls[0][0]); // 11
console.log(filterTestFn.mock.calls[1][0]); // 12
})

test('mockimplementation', ()=>{
    const myMockFn = jest.fn(cb => cb(null, true));

myMockFn((err, val) => console.log(val));
// > true
})


test('mockimplementationonce',()=> {
    const myMockFn = jest
  .fn(() => 'default')
  .mockImplementationOnce(() => 'first call')
  .mockImplementationOnce(() => 'second call');

console.log(myMockFn(), myMockFn(), myMockFn(), myMockFn());
// > 'first call', 'second call', 'default', 'default'
})


test('return this', ()=>{
    const myObj = {
        myMethod: jest.fn().mockReturnThis(),
      };
      
      // is the same as
      
      const otherObj = {
        myMethod: jest.fn(function () {
          return this;
        }),
      };
      console.log(myObj.myMethod())
      console.log(otherObj.myMethod())
})

test('mockName', ()=> {
    const myMockFn = jest
    .fn()
    .mockReturnValue('default')
    .mockImplementation(scalar => 42 + scalar)
    .mockName('add42'); 
    
   // expect(myMockFn).toBeCalled();
})


test('custom matchers', ()=>{
    const mockFunc= jest.fn();
        // The mock function was called at least once

    const arg1='arg1';
    const arg2='arg2';

    mockFunc(arg1, arg2);
    expect(mockFunc).toHaveBeenCalled();

    // The mock function was called at least once with the specified args
    expect(mockFunc).toHaveBeenCalledWith(arg1, arg2);

    // The last call to the mock function was called with the specified args
    expect(mockFunc).toHaveBeenLastCalledWith(arg1, arg2);

    // All calls and the name of the mock is written as a snapshot
    expect(mockFunc).toMatchSnapshot();
})

test('common matchers', ()=>{
    // The mock function was called at least once
const mockFunc= jest.fn().mockName('a mock name');

const arg1=42;
const arg2='arg2';

mockFunc(arg1, arg2); 
expect(mockFunc.mock.calls.length).toBeGreaterThan(0);

// The mock function was called at least once with the specified args
expect(mockFunc.mock.calls).toContainEqual([arg1, arg2]);

// The last call to the mock function was called with the specified args
expect(mockFunc.mock.calls[mockFunc.mock.calls.length - 1]).toEqual([
  arg1,
  arg2,
]);

// The first arg of the last call to the mock function was `42`
// (note that there is no sugar helper for this specific of an assertion)
expect(mockFunc.mock.calls[mockFunc.mock.calls.length - 1][0]).toBe(42);

// A snapshot will check that a mock was invoked the same number of times,
// in the same order, with the same arguments. It will also assert on the name.
expect(mockFunc.mock.calls).toEqual([[arg1, arg2]]);
expect(mockFunc.getMockName()).toBe('a mock name');
})