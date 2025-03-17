import { Schema, model } from 'mongoose';

const userSchema = new Schema({
    username: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    stories: [{ type: Schema.Types.ObjectId, ref: 'Story' }]
});

export default model('User', userSchema);