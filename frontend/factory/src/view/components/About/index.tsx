import React from 'react';
import classNames from 'classnames';
import { ru } from './i18n/ru.ts';
import styles from './index.module.scss';
import { ContentWrapper } from '../ContentWrapper';
import { Title } from '../UI/Text/Title';

const cx = classNames.bind(styles);

export const About: React.FC = () => {
    return (
        <ContentWrapper>
            <div className={cx(styles.wrapper)}>
                <Title name={ru.title} />
                <div className={cx(styles.description)}>{ru.description}</div>
            </div>
        </ContentWrapper>
    );
};
