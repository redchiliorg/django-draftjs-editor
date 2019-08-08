'use strict';

// Global target for exports.
var exports = window.Draft;

// Local identifiers of required modules.
var React = window.React;

/**
 * Button component to toggle styles in editor.
 *
 * @param props.onToggle: Function
 * @param props.style: string
 * @param props.label: Rect.Node
 */
exports.StyleButton = function StyleButton(props) {
    return React.createElement('span', {
        className: 'RichEditor-styleButton' + (
            props.active ? ' RichEditor-activeButton' : ''
        ),
        onMouseDown: function (event) {
            event.preventDefault();
            props.onToggle(props.style);
        },
    }, props.label);
};
