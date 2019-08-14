'use strict';

// Global target for exports.
var exports = window.Draft;

// Local identifiers of required modules.
var React = window.React;
var StyleButton = window.Draft.StyleButton;

/**
 * Style controls component.
 *
 * @param props.isActive: (style: string) => bool
 * @param props.onToggle: (style: string) => void
 * @param props.children: {label: string, style: string}[]
 * @returns {React.Node|null}
 */
exports.StyleControls = function StyleControls(props) {
    return props.children ? React.createElement('div', {
        className: 'RichEditor-controls'
    }, props.children.map(function (button) {
        return e(StyleButton, {
            key: button.style,
            active: props.isActive(button.style),
            onToggle: function() {
                props.onToggle(button.style);
            },
            label: button.label,
            style: button.style
        })
    })) : null;
};
