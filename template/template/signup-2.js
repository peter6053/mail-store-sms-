import React from 'react';

import Nav from '../components/Nav';
import SignupForm2 from '../components/SignupForm-2';

const Signup = () => {
  return (
    <>
      <div className="">
        <Nav />
      </div>
      <div className="pt-32">
        <div className="w-full md:w-11/12 lg:w-9/12 xl:w-8/12 mx-auto shadow-lg">
          <SignupForm2 />
        </div>
      </div>
    </>
  );
};

export default Signup;
