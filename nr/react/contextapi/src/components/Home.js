import faker from 'faker';

const Home = () => {
  const productArray = [...Array(20)].map(()=>({
    id:faker.datatype.uuid

  }));
  return (
    <div>
      Home
    </div>
  )
}

export default Home;