import express from 'express';
import mongoose from 'mongoose';
import authRoutes from './auth';
import storyRoutes from './story';

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 5000;

mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('Connected to MongoDB');
    app.listen(PORT, () => {
        console.log(`Server running on port ${PORT}`);
    });
}).catch(err => {
    console.error(err);
});

app.use('/api/auth', authRoutes);
app.use('/api/stories', storyRoutes);