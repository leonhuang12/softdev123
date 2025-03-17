import { Schema, model } from 'mongoose';

const storySchema = new Schema({
    title: { type: String, required: true },
    content: { type: String, required: true },
    latestUpdate: { type: String, required: true },
    contributors: [{ type: Schema.Types.ObjectId, ref: 'User' }]
});

export default model('Story', storySchema);