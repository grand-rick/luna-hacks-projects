var __spreadArrays = (this && this.__spreadArrays) || function () {
    for (var s = 0, i = 0, il = arguments.length; i < il; i++) s += arguments[i].length;
    for (var r = Array(s), k = 0, i = 0; i < il; i++)
        for (var a = arguments[i], j = 0, jl = a.length; j < jl; j++, k++)
            r[k] = a[j];
    return r;
};
var lowerAlphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
var upperAlphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
var numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
var special = ['!', '@', '#', '$', '%', '^', '&', '(', ')', '-', '_', '+'];
var PasswordGenerator = /** @class */ (function () {
    function PasswordGenerator() {
        this.passwordLength = 14;
        this.allCharacters = __spreadArrays(lowerAlphabets, upperAlphabets, numbers, special);
        this.password = '';
    }
    PasswordGenerator.prototype.getAllCharacters = function () {
        return this.allCharacters;
    };
    PasswordGenerator.prototype.getRandomPassword = function () {
        for (var i = 0; i < this.passwordLength; i++) {
            var randomInteger = Math.floor(Math.random() * this.allCharacters.length) + 1;
            this.password += this.allCharacters[randomInteger];
        }
        console.log(this.password);
        return this.password;
    };
    return PasswordGenerator;
}());
var passwordGenerator = new PasswordGenerator();
passwordGenerator.getRandomPassword();
