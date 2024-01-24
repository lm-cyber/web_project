import React from 'react';
import classNames from 'classnames';
import styles from './index.module.scss';
import { ru } from './i18n/ru.ts';
import { ContentWrapper } from '../ContentWrapper';
import { BenefitCard } from '../UI/Card/BenefitCard';

const cx = classNames.bind(styles);

export const Benefits: React.FC = () => {
    return (
        <div>
            <ContentWrapper>
                <div className={cx(styles.benefitsTable)}>
                    <div className={'col-span-2'}>
                        <BenefitCard name={ru.cards[0].name} description={ru.cards[0].description} />
                    </div>
                    <div className={'col-span-2 row-span-2'}>
                        <BenefitCard name={ru.cards[1].name} description={ru.cards[1].description} />
                    </div>
                    <div>
                        <BenefitCard name={ru.cards[2].name} description={ru.cards[2].description} />
                    </div>
                    <div>
                        <BenefitCard name={ru.cards[3].name} description={ru.cards[3].description} />
                    </div>
                </div>
            </ContentWrapper>
        </div>
    );
};
