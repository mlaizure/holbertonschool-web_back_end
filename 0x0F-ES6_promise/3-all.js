import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((vals) => {
      console.log(`${vals[0].body} ${vals[1].firstName} ${vals[1].lastName}`);
    }).catch(() => console.log('Signup system offline'));
}
