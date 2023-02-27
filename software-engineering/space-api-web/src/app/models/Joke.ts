export class Joke {
    error: boolean;
    category: string;
    type: string;
    setup: string;
    delivery: string;
    flags: {
        nsfw: boolean;
        religious: boolean;
        political: boolean;
        racist: boolean;
        sexist: boolean;
        explicit:boolean;
    };
    id: number;
    safe: boolean;
    lang: string;

    constructor () {
        this.error = false,
        this.category = '',
        this.type = '',
        this.setup = '',
        this.delivery = ''
        this.flags = {
            nsfw: false,
            religious: false,
            political: false,
            racist: false,
            sexist: false,
            explicit: false
        },
        this.id = 0,
        this.safe = true,
        this.lang = ''
    }
}