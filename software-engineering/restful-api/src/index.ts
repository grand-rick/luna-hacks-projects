import express, {Request, Response} from 'express';
import morgan from 'morgan';

const app = express();

const port = 3000;

app.use(morgan('common'));
app.get('/', (req: Request, res: Response) => {
    res.send('Home page!');
});

app.get('/about', (req: Request, res: Response) => {
    res.send('About Page');
})

app.listen(port, () => {
    console.log(`Server started at http://localhost:${port}`);
});
