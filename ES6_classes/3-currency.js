export default class Currency{
    constructor(code, name){
        this._code = code;
        this._name = name;
    }
    
    get code(){
        return this._code;
    }

    get name(){
        return this._name;
    }
}

export function displayFullCurrency(currency){
    return `${currency.name} (${currency.code})`;
}
