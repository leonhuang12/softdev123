import { Schema, model } from 'mongoose';

const contributionSchema = new Schema({
    user: { type: Schema.Types.ObjectId, ref: 'User', required: true },
    story: { type: Schema.Types.ObjectId, ref: 'Story', required: true },
    content: { type: String, required: true },
    date: { type: Date, default: Date.now }
});

export default model('Contribution', contributionSchema);