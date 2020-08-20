import React, { Fragment } from "react";
import './footer.css';
import logoimg from '../../templates/img/LogoIdeaTour.svg';


class Footer extends React.Component {
    state = {

    }
    render() {
        return(
            <Fragment>
                <div className="footer">
                    <div className="footer-left-side">

                        <div className="footer-container-ul">
                        <h6>Тури</h6>
                            <ul className="footer-ul-one">
                                <li>авіа тури</li>
                                <li>гарячі тури</li>
                                <li>автобусні тури</li>
                            </ul>
                        </div>

                        <div className="footer-container-ul">
                        <h6>Інформація</h6>
                            <ul className="footer-ul-two">
                                <li>як це працює</li>
                                <li>правова інформація</li>
                                <li>запитання відповіді</li>
                                <li>користувацька угода</li>
                            </ul>
                        </div>

                        <div className="footer-container-ul">
                        <h6>Про нас</h6>
                            <ul className="footer-ul-three">
                                <li>про нас</li>
                                <li>блог</li>
                                <li>контакти</li>
                            </ul>
                        </div>
                    </div>


                    <div className="foter-right-side">

                        <div className="footer-right-upper">
                            <div className="footer-contacts-part-one">
                                <div className="footer-phone">
                                    <h5 className="phone-number">0 800 500 505</h5>
                                    <p>з 9:00 до 22:00 щодня</p>
                                    <div className="foter-social">
                                        <i class="fab fa-instagram"></i>
                                        <i class="fab fa-facebook-f"></i>
                                        <i class="fab fa-telegram-plane"></i>
                                    </div>
                                </div>
                            </div>

                            <div className="footer-contacts-part-two">
                                <h5>рівне вул. соборна 67</h5>
                                <p>Пн-Пт з 10:00 до 19:00</p>
                                <p>Сб з 11:00 до 15:00</p>
                                <p>ideatur@ukr.net</p>
                            </div>
                        </div>

                        <div className="footer-right-down">
                            <input type="text" value="email"></input>
                            <button>підписатись</button>
                        </div>
                    </div>


                    <div className="footer-logo">
                        <img src={logoimg}></img>
                    </div>
                </div>
            </Fragment>
        )
    }
}
export default Footer
