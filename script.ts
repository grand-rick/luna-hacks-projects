const lowerAlphabets: string[] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

const upperAlphabets: string[] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

const numbers: string[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

const special: string[] = ['!', '@', '#', '$', '%', '^', '&', '(', ')', '-', '_', '+'];

class PasswordGenerator {
	passwordLength: number = 14;
	allCharacters: string[] = [
		...lowerAlphabets,
		...upperAlphabets,
		...numbers,
		...special
	];
	password: string = '';

	getAllCharacters():  string[] {
		return this.allCharacters;
	}

	getRandomPassword(): string {
		for (let i = 0; i < this.passwordLength; i++) {
			let randomInteger: number = Math.floor(Math.random() * this.allCharacters.length) + 1;
			this.password += this.allCharacters[randomInteger];
		}

		console.log(this.password);
		return this.password;
	}
}

const passwordGenerator = new PasswordGenerator();

passwordGenerator.getRandomPassword();