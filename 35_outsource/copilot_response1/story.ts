import { Router } from 'express';
import { createStory, addToStory, getUserStories } from './controllers/storyController';

const router = Router();

router.post('/create', createStory);
router.post('/add/:storyId', addToStory);
router.get('/user-stories', getUserStories);

export default router;