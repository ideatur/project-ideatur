import React, {Fragment} from "react";
import ReactDOM from 'react-dom';
import Header from './components/header/header';
import Main from './components/main/main';
import Footer from './components/footer/footer';


class App extends React.Component {
    state = {

    }
    render() {
        return (
            <Fragment>
                <Header/>
                <Main/>
                <Footer/>
            </Fragment>
        )
    }
}

ReactDOM.render(<App/>, document.getElementById('root'))